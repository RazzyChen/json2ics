import json
import re
from datetime import datetime, timedelta
import pytz
import uuid
import argparse

# 时区设置
shanghai_tz = pytz.timezone('Asia/Shanghai')

# 命令行参数解析
parser = argparse.ArgumentParser(description="将 JSON 学习计划转换为 iCalendar (.ics) 文件")
parser.add_argument('--input', type=str, default='study_plan.json', help='输入的 JSON 文件名（默认: study_plan.json）')
parser.add_argument('--output', type=str, default='study_plan.ics', help='输出的 ICS 文件名（默认: study_plan.ics）')
args = parser.parse_args()

# 读取 JSON 文件
try:
    with open(args.input, 'r', encoding='utf-8') as f:
        data = json.load(f)
except FileNotFoundError:
    print(f"❌ 错误：找不到文件 {args.input}")
    exit(1)

# 初始化 ICS 内容
ics_content = [
    "BEGIN:VCALENDAR",
    "VERSION:2.0",
    "PRODID:-//My Learning Plan//Calendar Export//EN"
]

# 处理每个学习计划条目
for event in data['学习计划']:
    course = event.get("学习课程", "")
    duration = event.get("学习时长", "")
    date_str = event.get("学习日期", "")

    # 跳过空事件
    if not course and not duration:
        continue

    # 解析日期
    match = re.match(r'(\d+)月(\d+)日', date_str)
    if not match:
        continue  # 跳过无效日期格式
    month = int(match.group(1))
    day = int(match.group(2))
    year = 2025  # 假设年份为 2025

    # 解析时间
    if duration == "1h":
        start_time = datetime(year, month, day, 12, 0)
        end_time = start_time + timedelta(hours=1)
    else:
        times = duration.split('-')
        if len(times) != 2:
            continue
        start_str, end_str = times
        start_h, start_m = map(int, start_str.split(':'))
        end_h, end_m = map(int, end_str.split(':'))
        start_time = datetime(year, month, day, start_h, start_m)
        end_time = datetime(year, month, day, end_h, end_m)

    # 设置时区
    start_time = shanghai_tz.localize(start_time, is_dst=None)
    end_time = shanghai_tz.localize(end_time, is_dst=None)

    # 格式化为 ICS 时间格式
    dtstart = start_time.strftime("%Y%m%dT%H%M%S")
    dtend = end_time.strftime("%Y%m%dT%H%M%S")

    # 生成时间戳（使用 timezone-aware 的 UTC 时间）
    now_utc = datetime.now(tz=pytz.utc).strftime("%Y%m%dT%H%M%SZ")

    # 构建 UID
    uid = str(uuid.uuid4()).upper()

    # 构建 ICS 事件
    ics_event = [
        "BEGIN:VEVENT",
        f"DTSTART;TZID=Asia/Shanghai:{dtstart}",
        f"DTEND;TZID=Asia/Shanghai:{dtend}",
        f"DTSTAMP:{now_utc}",
        f"CREATED:{now_utc}",
        f"LAST-MODIFIED:{now_utc}",
        "SEQUENCE:0",
        f"SUMMARY:{course}",
        "TRANSP:OPAQUE",
        f"UID:{uid}",
        "X-APPLE-CREATOR-IDENTITY:com.apple.calendar",
        "X-APPLE-CREATOR-TEAM-IDENTITY:0000000000",
        "END:VEVENT"
    ]

    ics_content.extend(ics_event)

# 结束日历
ics_content.append("END:VCALENDAR")

# 写入 ICS 文件
with open(args.output, 'w', encoding='utf-8') as f:
    f.write('\n'.join(ics_content))

print(f"✅ ICS 文件已成功生成：{args.output}")