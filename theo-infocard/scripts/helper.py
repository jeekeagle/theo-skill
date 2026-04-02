#!/usr/bin/env python3
"""示例辅助脚本"""

import argparse


def main():
    parser = argparse.ArgumentParser(description="示例辅助脚本")
    parser.add_argument("--option", help="选项说明")
    args = parser.parse_args()

    print(f"执行示例脚本，选项: {args.option}")


if __name__ == "__main__":
    main()
