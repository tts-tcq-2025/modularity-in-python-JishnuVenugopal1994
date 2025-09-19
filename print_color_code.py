from color_code import MAJOR_COLORS, MINOR_COLORS, get_color_from_pair_number

def get_color_coding_manual():
  manual_lines = []
  total_pairs = len(MAJOR_COLORS) * len(MINOR_COLORS)
  manual_lines.append("Pair No. | Major Color | Minor Color")
  manual_lines.append("-" * 32)
  for pair_number in range(1, total_pairs + 1):
    major_color, minor_color = get_color_from_pair_number(pair_number)
    manual_lines.append(f"{pair_number:7} | {major_color:11} | {minor_color}")
  return "\n".join(manual_lines)