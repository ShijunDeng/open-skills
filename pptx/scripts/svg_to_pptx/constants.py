"""SVG to PPTX 目录与格式常量"""
from pathlib import Path

# Skill root (three levels up: svg_to_pptx/ -> scripts/ -> pptx/)
DEFAULT_PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

# 标准子目录名称
DIR_SVG_OUTPUT = 'svg_output'
DIR_SVG_FINAL = 'svg_final'
DIR_SVG_ROUNDED = 'svg_rounded'
DIR_PAGES = 'pages'
DIR_OUTPUT = 'output'

# 目录别名映射（source alias -> 实际目录名）
DIR_ALIAS_MAP = {
    'pages': DIR_PAGES,       # SKILL.md 标准目录
    'output': DIR_SVG_OUTPUT,
    'final': DIR_SVG_FINAL,
    'flat': 'svg_output_flattext',
    'final_flat': 'svg_final_flattext',
}
