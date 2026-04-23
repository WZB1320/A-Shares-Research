# tools/utils.py
def calc_percentile(history, current):
    """
    计算历史分位的通用工具函数
    """
    if not history:
        return 0
    arr = sorted(history)
    cnt = sum(1 for v in arr if v <= current)
    return round(cnt / len(arr) * 100, 2)