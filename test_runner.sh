#!/bin/bash

# BMI 計算機測試腳本

echo "=== BMI 計算機測試腳本 ==="
echo ""

# 設定 Python 執行路径
PYTHON_CMD="/workspaces/20250716-GH900/.venv/bin/python"

echo "1. 執行所有單元測試"
echo "===================="
$PYTHON_CMD -m unittest test_bmi.py -v
echo ""

echo "2. 測試 BMI 計算功能"
echo "===================="
echo "測試公制單位: 70公斤, 175公分"
$PYTHON_CMD -c "
from app import calculate_bmi_metric, classify_bmi
bmi = calculate_bmi_metric(70, 175)
classification = classify_bmi(bmi)
print(f'BMI: {bmi}')
print(f'分類: {classification}')
"
echo ""

echo "測試英制單位: 154磅, 69英吋"
$PYTHON_CMD -c "
from app import calculate_bmi_imperial, classify_bmi
bmi = calculate_bmi_imperial(154, 69)
classification = classify_bmi(bmi)
print(f'BMI: {bmi}')
print(f'分類: {classification}')
"
echo ""

echo "3. 測試錯誤處理"
echo "=================="
echo "測試無效輸入 (負數):"
$PYTHON_CMD -c "
try:
    from app import calculate_bmi_metric
    calculate_bmi_metric(-10, 175)
except ValueError as e:
    print(f'✅ 成功捕獲錯誤: {e}')
"

echo "測試無效輸入 (零值):"
$PYTHON_CMD -c "
try:
    from app import calculate_bmi_metric
    calculate_bmi_metric(70, 0)
except ValueError as e:
    print(f'✅ 成功捕獲錯誤: {e}')
"
echo ""

echo "4. 測試邊界值"
echo "=================="
echo "測試各種 BMI 分類:"
$PYTHON_CMD -c "
from app import classify_bmi
test_cases = [
    (17.5, '體重過輕'),
    (18.5, '正常體重'),
    (24.9, '正常體重'),
    (25.0, '體重過重'),
    (29.9, '體重過重'),
    (30.0, '肥胖')
]
for bmi, expected in test_cases:
    result = classify_bmi(bmi)
    status = '✅' if result == expected else '❌'
    print(f'{status} BMI {bmi}: {result} (預期: {expected})')
"
echo ""

echo "=== 測試完成 ==="
