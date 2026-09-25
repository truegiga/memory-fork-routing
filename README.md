# memory-fork-routing

A WorkBuddy skill that gives you **local, auditable control over your agent's memory**: turn off uncontrollable cloud memory, slim your main `MEMORY.md` down to a pure routing layer with a **six-fork routing tree**, and keep it honest with a **memory usage ledger + periodic human review**.

中文说明见下方 [中文说明](#中文说明)。

## Why

- Cloud memory cannot be precisely controlled: it auto-picks content from your context nightly to build a "user profile" that only grows. Worse, transformers handle "don't mention X" poorly — the more you emphasize what not to say, the more salient it becomes.
- Memory effectiveness cannot be managed by effectiveness scores or weights. **The most effective memory is often the one that works silently.** What you need is a ledger that answers: "this rule was injected, yet the mistake still happened — why?"

## Core ideas (three moves)

1. **Turn off cloud memory.** Core memory stays local. (The skill gives manual instructions; it never flips your settings silently.)
2. **Six-fork routing tree + routing pointers.** Fork memory triggers by "the action I'm about to take" (talk / build / calculate / act / look up / self-modify). Parent nodes fully contain child nodes; the main `MEMORY.md` holds only routing pointers, all rules sink into `knowledge/01–06` second-level files. Hard red lines load every session via a `SessionStart` hook — never rely on model self-discipline.
3. **Usage ledger + human review.** Every red line hit / miss / waste is logged as one mechanical line. Memory fixes require human review — otherwise you've just rebuilt the cloud system you turned off.

## How it works

Semi-automatic, guided session — the skill never writes your memory silently:

```
Stage 0    Environment detection (real commands, no assumptions)
Stage 0.5  Conflict self-check (if you already have a MEMORY.md)
Stage A    Skeleton setup (copies assets/ templates, backs up before overwrite)
Stage B    Guided filling (choose starting branch: migrate old memory / start fresh;
           template + desensitized example for each item, capped total volume)
Stage C    Cloud-memory off guide + SessionStart hook setup
```

## Repository layout

```
SKILL.md                        # main skill instructions (stages 0–C)
PUBLISH.md                      # publishing notes & troubleshooting
_meta.json                      # skill metadata
assets/MEMORY.md                # template: routing-layer main memory
assets/hooks/session-start-inject.py  # SessionStart injection script
assets/knowledge/01–06.md       # six-fork rule files (dialogue/output/calc/local/lookup/system)
assets/memory-usage-ledger.md   # template: hit / miss / waste ledger
```

**Portability statement**: this distributes a *methodology scaffold*, not anyone's personal memory. The templates ship empty or with desensitized examples.

## Install

WorkBuddy: import via the skills manager, or:

```bash
npx skills add truegiga/memory-fork-routing --skill memory-fork-routing
```

Manual: copy the folder to `~/.workbuddy/skills/memory-fork-routing/`.

## Requirements

- A WorkBuddy-class client with local-file memory and `SessionStart` hook support
- macOS / Windows / Linux (the skill detects your OS and picks shell dialects accordingly)

## Usage triggers

Say things like: 「整理记忆 / 记忆重构 / 六分叉 / memory 路由 / 关云端记忆 / 记忆瘦身」, or type `/memory-fork-routing`.

---

## 中文说明

**这是什么**：一个 WorkBuddy skill，把 Agent 记忆的主动权收回本地：关掉不可控的云端记忆，用「六分叉路由 + 路由指针」把主 `MEMORY.md` 瘦身为纯索引层，规则全部下沉到 `knowledge/01–06` 二级文件，再用「memory 台账 + 定期人工审核」保证每条记忆真的在起作用。

**为什么**：云端记忆每晚自动从上下文里挑内容生成「用户画像」且越攒越长，无法精确控制；而模型对「用户禁止某事」的注意力处理很差——越强调越记得清。同时，记忆有效性**不能靠评分/权重管理**：最有效的那条记忆往往是永远静默生效的那条，能管住它的只有「命中/漏报/空转」台账加人工审核。

**怎么用**：安装后开新会话，说「整理记忆」或输入 `/memory-fork-routing`。流程是半自动引导式的：先铺空骨架，再逐项给模板和脱敏示例，你确认后才落盘，绝不静默代写，填写总量有封顶。

**本仓库只分发方法论骨架**（空模板 + 脱敏示例），不含任何个人记忆内容。

---

Author: Sean Cai
