# 获取 PR 修改的文件
modified_files = git.modified_files + git.added_files
deleted_files = git.deleted_files

# 计算 PR 修改的行数
total_lines_changed = git.lines_of_code

# **分析涉及的模块**
module_mapping = {
  "./github/workflows" => "📃 GitHub 模块",
  "src/network" => "🌐 网络模块",
  "src/db" => "🗄️ 数据库模块",
  "src/ui" => "🎨 前端 UI",
  "public" => "🎨 设计资源",
  "assets" => "🖼️ 图片/图标",
  "styles" => "🎨 样式文件（CSS/SCSS）",
  "config" => "⚙️ 配置文件",
  "tests" => "🧪 测试代码",
  "scripts" => "🔧 脚本工具",
  "docs" => "📖 文档"
}

# 找出受影响的模块
affected_modules = modified_files
  .map { |file| module_mapping.find { |path, _| file.start_with?(path) } }
  .compact
  .map(&:last)
  .uniq

# 生成 PR 摘要
summary = "### 🤖 PR 自动摘要\n"
summary += "- 影响的文件数量：#{modified_files.count + deleted_files.count}\n"
summary += "- 新增文件：#{git.added_files.count}\n"
summary += "- 修改文件：#{git.modified_files.count}\n"
summary += "- 删除文件：#{git.deleted_files.count}\n"
summary += "- 代码变更总行数：#{total_lines_changed}\n"

# 列出主要修改的文件
unless modified_files.empty?
  summary += "\n### 📝 主要修改文件：\n"
  modified_files.first(5).each { |file| summary += "- `#{file}`\n" }
end

# 列出主要删除的文件
unless deleted_files.empty?
  summary += "\n### ❌ 主要删除文件：\n"
  deleted_files.first(5).each { |file| summary += "- `#{file}`\n" }
end

# 列出受影响的模块
unless affected_modules.empty?
  summary += "\n### 📌 影响的模块：\n"
  affected_modules.each { |mod| summary += "- #{mod}\n" }
end

# 检查 PR 描述是否填写
if github.pr_body.nil? || github.pr_body.strip.empty?
  warn("⚠️ PR 描述为空，请补充详细的修改说明。")
end

# 检测是否直接向 master 分支提交
if github.branch == "master"
  warn("🚨 **警告：PR 直接提交到 master 分支，请确认是否符合流程！**")
end

# 在 PR 页面评论这个摘要
markdown(summary)
