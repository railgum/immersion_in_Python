import os
import glob


def rm_files(dir_name: str,
             ext_origin: str,
             ext_final: str,
             list_origin_band: list,
             desired_name: str = 'file',
             digit_numbers: int = 2):
    count = 1
    for item_file in glob.iglob(os.path.join(dir_name, ext_origin)):
        count_str = str(count).zfill(digit_numbers)
        name, ext = os.path.splitext(os.path.basename(item_file))
        os.rename(item_file,
                  os.path.join(dir_name, f'{name[list_origin_band[0]:list_origin_band[1]]}_{desired_name}_{count_str}{ext_final}'))
        count += 1
