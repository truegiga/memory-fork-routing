# 发布到 GitHub（由你自行操作，本 skill 不会自动上传）

> 安全提示：本仓库的 `assets/` 全部是**空骨架模板**，不含任何私人记忆内容，可以放心公开。
> 发布前请最后确认一遍：没有把 `~/.workbuddy/MEMORY.md`、`knowledge/`、`memory-usage-ledger.md` 的**真实内容**误拷进 `assets/`。

## 步骤

### 1. 在本地初始化仓库（在 skill 文件夹内）
```bash
cd /Users/sean/WorkBuddy/个人学习工作经验积累/memory-fork-routing-skill
git init
git add .
git commit -m "feat: memory-fork-routing scaffold skill"
```

### 2. 在 GitHub 建仓库并推送
方式 A（网页）：登录 GitHub → New repository → 命名为 `memory-fork-routing` → **不要勾选创建仓库页面里的「Add README」开关**（其描述为 "READMEs can be used as longer descriptions"，下方的 "About READMEs" 链接即 GitHub 官方说明；勾选会让远端先有一个初始 commit，与你本地 `git init` 已提交的历史冲突，导致后续 `git push -u origin main` 被拒）→ 复制仓库 URL。
方式 B（CLI，需 gh 已登录）：`gh repo create memory-fork-routing --public --source=. --push`

然后（若用方式 A）：
```bash
git branch -M main
git remote add origin https://github.com/<你的用户名>/memory-fork-routing.git
git push -u origin main
```

### 3. 别人如何安装
```bash
npx skills add <你的用户名>/memory-fork-routing --skill memory-fork-routing -g -y
```
安装后调用 skill（说「整理记忆 / 记忆重构 / 六分叉 / memory 路由 / 关云端记忆 / 建 memory 台账 / 记忆瘦身」之一即可），它会：
1. **阶段 A 自动铺骨架**：把 `assets/` 空模板一键铺到 `~/.workbuddy/`（带备份，不覆盖现有文件）；
2. **阶段 B 会话式引导填写**：逐项给模板+脱敏示例，你确认后才落盘（硬红线 → 六分叉规则 → 强制注入分叉 → 启用台账）；
3. **阶段 C 指引**：手动关云端记忆 + 可选授权后合并 hook 配置。
全程半自动，不静默代写你的私人内容。

### 4. （可选）上架 SkillHub / ClawHub
- SkillHub：在 https://lightmake.site 提交仓库地址，按引导填写 description（已写在 SKILL.md frontmatter）。
- 描述里务必保留「仅适用于 WorkBuddy 类本地 memory 体系 / 分发的是框架骨架而非私人记忆」的可移植性声明。

## 常见问题 / 故障排查

### push 时报 `Invalid username or token. Password authentication is not supported`
GitHub 自 2021-08 起已**停用账号密码**做 git 验证。终端提示 Password 时，必须填 **Personal Access Token（PAT）**，不是登录密码。
1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic) → Generate new token：勾选 `repo` scope，生成后**立即复制**（只显示一次）。
2. 重新 `git push -u origin main`：`Username` 填 GitHub 用户名，`Password` 处**粘贴 token**。
3. 若 macOS 之前缓存了错误密码导致秒失败：执行 `printf "protocol=https\nhost=github.com\n" | git credential-osxkeychain erase` 清缓存，或去「钥匙串访问」删 `github.com` 条目。
- **更省事**：先 `gh auth login`（浏览器授权），之后 `git push` 不再要密码/token；或改用 SSH（`git@github.com:用户名/memory-fork-routing.git`）。
