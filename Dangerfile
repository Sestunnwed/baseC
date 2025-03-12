# Get the modified, added, and deleted files in the PR
modified_files = git.modified_files + git.added_files
deleted_files = git.deleted_files

# Calculate total lines changed in the PR
total_lines_changed = git.lines_of_code

# Generate PR summary
summary = "### 🤖 PR Auto Summary\n"
summary += "🚀 **Total affected files**: #{modified_files.count + deleted_files.count}\n"
summary += "🆕 **New files**: #{git.added_files.count}\n"
summary += "✏️ **Modified files**: #{git.modified_files.count}\n"
summary += "🗑️ **Deleted files**: #{git.deleted_files.count}\n"
summary += "📊 **Total lines changed**: #{total_lines_changed}\n"
summary += "📂 **Key modified files**:\n"

modified_files.first(5).each do |file|
  summary += "  - `#{file}`\n"
end

unless deleted_files.empty?
  summary += "🗂️ **Key deleted files**:\n"
  deleted_files.first(5).each do |file|
    summary += "  - `#{file}`\n"
  end
end

# Warn if PR description is empty
warn("PR description is empty. Please provide a detailed explanation of the changes.") if github.pr_body.nil? || github.pr_body.strip.empty?

source_branch = github.branch_for_head
target_branch = github.branch_for_base

# Warn if PR target branch is main/master and source is not dev/develop
warn("PR target branch is `#{target_branch}`. Ensure this PR follows the merge strategy!") if (target_branch == "main" || target_branch == "master") && !(source_branch == "dev" || source_branch == "develop")

# Warn if PR is still a work in progress
warn("PR is marked as Work in Progress (WIP).") if github.pr_title.include? "WIP"

# Warn if PR has no labels
warn("Please add labels to this PR.") if github.pr_labels.empty?

# Post the summary as a comment on the PR
markdown(summary)

# 获取 PR 中修改的 Python 文件
python_files = (git.modified_files + git.added_files).select { |file| file.end_with?(".py") }

unless python_files.empty?
  flake8_result = `flake8 #{python_files.join(" ")}`
  flake8_exit_status = $?.exitstatus

  if flake8_exit_status != 0
    fail("❌ Flake8 code issues found:\n```\n#{flake8_result}\n```")
  else
    message("✅ No Flake8 issues found!")
  end

  pylint_result = `pylint --output-format=parseable #{python_files.join(" ")}`
  pylint_exit_status = $?.exitstatus

  if pylint_exit_status != 0
    fail("❌ Pylint issues found:\n```\n#{pylint_result}\n```")
  else
    message("✅ No Pylint issues found!")
  end
end
