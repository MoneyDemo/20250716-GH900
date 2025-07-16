# BMI 計算機 (Body Mass Index Calculator)

這是一個使用 Python 撰寫的身體質量指數 (BMI) 計算機，支援公制和英制單位，包含完整的單元測試。

## 功能特色

- 🏥 **雙單位支援**: 支援公制 (公斤/公分) 和英制 (磅/英吋) 單位
- 📊 **BMI 分類**: 自動分類體重狀態 (體重過輕/正常體重/體重過重/肥胖)
- 💡 **健康建議**: 根據 BMI 結果提供相應的健康建議
- ✅ **完整測試**: 包含全面的單元測試和整合測試
- 🛡️ **錯誤處理**: 完善的輸入驗證和錯誤處理機制
- 🌏 **中文介面**: 完全中文化的使用者介面

## BMI 計算公式

### 公制單位
```
BMI = 體重(公斤) / [身高(公尺)]²
```

### 英制單位
```
BMI = (體重(磅) × 703) / [身高(英吋)]²
```

## BMI 分類標準

| BMI 範圍 | 分類 | 健康狀態 |
|----------|------|----------|
| < 18.5 | 體重過輕 | 可能營養不良 |
| 18.5 - 24.9 | 正常體重 | 健康範圍 |
| 25.0 - 29.9 | 體重過重 | 過重風險 |
| ≥ 30.0 | 肥胖 | 高健康風險 |

## 檔案結構

```
📦 BMI Calculator
├── 📄 app.py           # 主程式檔案
├── 📄 test_bmi.py      # 單元測試檔案
├── 📄 README.md        # 說明文件
└── 📄 LICENSE          # 授權檔案
```

## 安裝與執行

### 系統需求

- Python 3.6 或更新版本
- 無需額外套件 (使用 Python 標準函式庫)

### 執行主程式

```bash
# 方法 1: 直接執行
python app.py

# 方法 2: 作為模組執行
python -m app
```

### 程式使用流程

1. 選擇單位系統 (公制或英制)
2. 輸入體重和身高
3. 查看 BMI 計算結果和分類
4. 參考健康建議

### 使用範例

```
=== BMI 計算機 ===
選擇單位系統:
1. 公制 (公斤/公分)
2. 英制 (磅/英吋)
請選擇 (1 或 2): 1
請輸入體重 (公斤): 70
請輸入身高 (公分): 175

=== 計算結果 ===
您的 BMI 值: 22.86
體重狀態: 正常體重
建議: 維持現在的生活習慣，保持健康體重
```

## 執行測試

### 快速測試

執行所有測試：

```bash
python -m unittest test_bmi.py
```

### 詳細測試輸出

執行測試並顯示詳細資訊：

```bash
python -m unittest test_bmi.py -v
```

### 執行特定測試類別

```bash
# 測試 BMI 計算功能
python -m unittest test_bmi.TestBMICalculator -v

# 測試整合功能
python -m unittest test_bmi.TestBMIIntegration -v
```

### 執行特定測試方法

```bash
# 測試公制 BMI 計算
python -m unittest test_bmi.TestBMICalculator.test_calculate_bmi_metric_normal_cases -v

# 測試 BMI 分類
python -m unittest test_bmi.TestBMICalculator.test_classify_bmi -v

# 測試無效輸入處理
python -m unittest test_bmi.TestBMICalculator.test_calculate_bmi_metric_invalid_input -v
```

### 測試覆蓋率

如果您想查看測試覆蓋率，可以安裝並使用 `coverage` 工具：

```bash
# 安裝 coverage 工具
pip install coverage

# 執行測試並收集覆蓋率資料
coverage run -m unittest test_bmi.py

# 查看覆蓋率報告
coverage report

# 生成 HTML 覆蓋率報告
coverage html
```

## 測試說明

### 測試內容

我們的測試套件包含以下測試：

#### 1. 功能測試
- ✅ **公制 BMI 計算**: 測試各種體重和身高組合
- ✅ **英制 BMI 計算**: 測試英制單位的計算準確性
- ✅ **BMI 分類**: 測試所有 BMI 分類範圍
- ✅ **邊界值測試**: 測試分類邊界的準確性

#### 2. 錯誤處理測試
- ✅ **無效輸入**: 零值、負值輸入的錯誤處理
- ✅ **例外處理**: 確保適當的例外被拋出
- ✅ **輸入驗證**: 驗證輸入資料的合理性

#### 3. 整合測試
- ✅ **完整流程**: 測試從輸入到輸出的完整計算流程
- ✅ **單位一致性**: 驗證公制和英制計算的一致性
- ✅ **結果格式**: 確保輸出格式正確

### 測試數據

測試使用了多組真實的測試數據：

```python
# 公制測試數據 (體重kg, 身高cm, 預期BMI)
(70, 175, 22.86)  # 正常體重
(50, 160, 19.53)  # 正常體重
(45, 170, 15.57)  # 體重過輕
(85, 170, 29.41)  # 體重過重
(100, 165, 36.73) # 肥胖
```

### 預期測試結果

執行測試時，您應該看到類似的輸出：

```
test_calculate_bmi_imperial_edge_cases (__main__.TestBMICalculator) ... ok
test_calculate_bmi_imperial_invalid_input (__main__.TestBMICalculator) ... ok
test_calculate_bmi_imperial_normal_cases (__main__.TestBMICalculator) ... ok
test_calculate_bmi_metric_edge_cases (__main__.TestBMICalculator) ... ok
test_calculate_bmi_metric_invalid_input (__main__.TestBMICalculator) ... ok
test_calculate_bmi_metric_normal_cases (__main__.TestBMICalculator) ... ok
test_bmi_calculation_consistency (__main__.TestBMICalculator) ... ok
test_bmi_result_format (__main__.TestBMICalculator) ... ok
test_classify_bmi (__main__.TestBMICalculator) ... ok
test_classify_bmi_boundary_values (__main__.TestBMICalculator) ... ok
test_complete_workflow_imperial (__main__.TestBMIIntegration) ... ok
test_complete_workflow_metric (__main__.TestBMIIntegration) ... ok

----------------------------------------------------------------------
Ran 12 tests in 0.XXXs

OK
```

## 開發與貢獻

### 程式碼結構

- `calculate_bmi_metric()`: 公制 BMI 計算
- `calculate_bmi_imperial()`: 英制 BMI 計算
- `classify_bmi()`: BMI 分類功能
- `get_user_input()`: 使用者輸入處理
- `main()`: 主程式邏輯

### 新增功能

如果您想新增功能，請確保：

1. 為新功能撰寫對應的測試
2. 更新文件說明
3. 確保所有現有測試仍然通過
4. 遵循現有的程式碼風格

### 常見問題

**Q: 為什麼有些測試使用 `assertAlmostEqual`？**
A: 因為浮點數計算可能有精度問題，特別是在單位轉換時。

**Q: 如何新增更多的 BMI 分類？**
A: 修改 `classify_bmi()` 函數並在 `test_classify_bmi()` 中新增對應測試。

**Q: 可以新增其他單位嗎？**
A: 可以！按照現有的模式新增計算函數，並撰寫對應測試。

## 授權

此專案採用 MIT 授權 - 詳見 [LICENSE](LICENSE) 檔案。

## 健康免責聲明

⚠️ **重要提醒**: 此 BMI 計算機僅供參考，不能替代專業醫療建議。BMI 指標有其局限性，不適用於：

- 孕婦
- 18歲以下兒童和青少年
- 肌肉量較高的運動員
- 年長者

如有健康疑慮，請諮詢合格的醫療專業人員。
