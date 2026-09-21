#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SessionStart hook 模板（通用版）
================================
在会话创建、模型读到用户第一条消息之前，由宿主执行本脚本。
只做一件事：读 FILES 列表里的文件 -> 向 stdout 吐一行 JSON，宿主把它注入上下文。
只读、无副作用、绝不抛异常、exit 0。

为什么需要它：
  会话第一轮自动进上下文的只有 MEMORY.md 主文件（路由层）。
  knowledge/ 各分叉细则不在其中，只能靠模型主动去读 -> 第一条消息可能不受细则约束。
  本 hook 强制注入你标记为「必须每次加载」的分叉，不依赖模型自觉。

如何配置：
  1. 把本文件放到 ~/.workbuddy/hooks/ 下（macOS/Linux 需 `chmod +x`；Windows 由 settings.json 的 command 用 `python` 显式调起，无需 chmod）。路径里统一用 `os.path.expanduser("~")`，脚本会自动展开成各 OS 的真实 home，无需手写绝对路径。
  2. 在 ~/.workbuddy/settings.json 加入 hooks.SessionStart 片段（见 SKILL.md 第 4 节）。
  3. 在下方 FILES 里增删你要强制注入的文件（注意：每加一个都会占用每次会话的上下文）。
"""

import json
import os
import sys

# 默认只强制注入路由层 MEMORY.md。
# 想让某个分叉每次都加载，把它加进这个列表，例如：
#   os.path.expanduser("~/.workbuddy/knowledge/01-dialogue.md"),
FILES = [
    os.path.expanduser("~/.workbuddy/MEMORY.md"),
]


def main():
    parts = []
    for path in FILES:
        try:
            with open(path, encoding="utf-8") as fh:
                parts.append(
                    "<!-- injected by SessionStart hook: %s -->\n%s" % (path, fh.read())
                )
        except Exception as exc:  # 读不到也不能阻断会话
            parts.append("<!-- inject failed: %s (%s) -->" % (path, exc))

    out = {"continue": True}
    if parts:
        out["hookSpecificOutput"] = {
            "hookEventName": "SessionStart",
            "additionalContext": "\n\n".join(parts),
        }

    try:
        sys.stdout.write(json.dumps(out, ensure_ascii=False))
        sys.stdout.write("\n")
    except Exception:
        sys.stdout.write('{"continue": true}\n')


if __name__ == "__main__":
    try:
        main()
    except Exception:
        sys.stdout.write('{"continue": true}\n')
    sys.exit(0)
