# 快速測試指令

## 基本測試指令

### 執行所有測試
```bash
python -m unittest test_bmi.py
```

### 詳細測試輸出
```bash
python -m unittest test_bmi.py -v
```

### 執行完整測試腳本
```bash
./test_runner.sh
```

## 手動測試 BMI 計算

### 測試公制計算
```bash
python -c "from app import calculate_bmi_metric, classify_bmi; bmi = calculate_bmi_metric(70, 175); print(f'BMI: {bmi}, 分類: {classify_bmi(bmi)}')"
```

### 測試英制計算
```bash
python -c "from app import calculate_bmi_imperial, classify_bmi; bmi = calculate_bmi_imperial(154, 69); print(f'BMI: {bmi}, 分類: {classify_bmi(bmi)}')"
```

## 執行主程式
```bash
python app.py
```

## 常用測試組合

### 快速驗證所有功能
```bash
python -m unittest test_bmi.py && echo "所有測試通過！"
```

### 檢查特定測試類別
```bash
python -m unittest test_bmi.TestBMICalculator -v
python -m unittest test_bmi.TestBMIIntegration -v
```
