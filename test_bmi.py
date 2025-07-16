"""
BMI 計算機的單元測試
使用 unittest 框架進行測試
"""

import unittest
import sys
import os

# 將當前目錄添加到系統路徑，以便導入 app 模組
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import calculate_bmi_metric, calculate_bmi_imperial, classify_bmi


class TestBMICalculator(unittest.TestCase):
    """BMI 計算機測試類別"""
    
    def setUp(self):
        """測試前的設置"""
        self.test_cases_metric = [
            # (體重kg, 身高cm, 預期BMI)
            (70, 175, 22.86),  # 正常體重
            (50, 160, 19.53),  # 正常體重
            (45, 170, 15.57),  # 體重過輕
            (85, 170, 29.41),  # 體重過重
            (100, 165, 36.73), # 肥胖
        ]
        
        self.test_cases_imperial = [
            # (體重lbs, 身高inches, 預期BMI)
            (154, 69, 22.75),  # 正常體重 (70kg, 175cm)
            (110, 63, 19.48),  # 正常體重 (50kg, 160cm) - 修正數值
            (99, 67, 15.51),   # 體重過輕 (45kg, 170cm)
            (187, 67, 29.30),  # 體重過重 (85kg, 170cm)
            (220, 65, 36.63),  # 肥胖 (100kg, 165cm)
        ]

    def test_calculate_bmi_metric_normal_cases(self):
        """測試公制 BMI 計算的正常情況"""
        for weight, height, expected_bmi in self.test_cases_metric:
            with self.subTest(weight=weight, height=height):
                result = calculate_bmi_metric(weight, height)
                self.assertAlmostEqual(result, expected_bmi, places=2,
                                     msg=f"BMI計算錯誤: 體重{weight}kg, 身高{height}cm")

    def test_calculate_bmi_imperial_normal_cases(self):
        """測試英制 BMI 計算的正常情況"""
        for weight, height, expected_bmi in self.test_cases_imperial:
            with self.subTest(weight=weight, height=height):
                result = calculate_bmi_imperial(weight, height)
                self.assertAlmostEqual(result, expected_bmi, places=2,
                                     msg=f"BMI計算錯誤: 體重{weight}lbs, 身高{height}inches")

    def test_calculate_bmi_metric_edge_cases(self):
        """測試公制 BMI 計算的邊界情況"""
        # 測試最小值
        result = calculate_bmi_metric(0.1, 50)
        self.assertGreater(result, 0)
        
        # 測試很高的人
        result = calculate_bmi_metric(80, 220)
        self.assertGreater(result, 0)

    def test_calculate_bmi_imperial_edge_cases(self):
        """測試英制 BMI 計算的邊界情況"""
        # 測試最小值
        result = calculate_bmi_imperial(0.1, 20)
        self.assertGreater(result, 0)
        
        # 測試很高的人
        result = calculate_bmi_imperial(180, 87)
        self.assertGreater(result, 0)

    def test_calculate_bmi_metric_invalid_input(self):
        """測試公制 BMI 計算的無效輸入"""
        # 測試零值
        with self.assertRaises(ValueError):
            calculate_bmi_metric(0, 170)
        
        with self.assertRaises(ValueError):
            calculate_bmi_metric(70, 0)
        
        # 測試負值
        with self.assertRaises(ValueError):
            calculate_bmi_metric(-10, 170)
        
        with self.assertRaises(ValueError):
            calculate_bmi_metric(70, -170)

    def test_calculate_bmi_imperial_invalid_input(self):
        """測試英制 BMI 計算的無效輸入"""
        # 測試零值
        with self.assertRaises(ValueError):
            calculate_bmi_imperial(0, 70)
        
        with self.assertRaises(ValueError):
            calculate_bmi_imperial(150, 0)
        
        # 測試負值
        with self.assertRaises(ValueError):
            calculate_bmi_imperial(-10, 70)
        
        with self.assertRaises(ValueError):
            calculate_bmi_imperial(150, -70)

    def test_classify_bmi(self):
        """測試 BMI 分類功能"""
        # 測試體重過輕
        self.assertEqual(classify_bmi(17.5), "體重過輕")
        self.assertEqual(classify_bmi(18.4), "體重過輕")
        
        # 測試正常體重
        self.assertEqual(classify_bmi(18.5), "正常體重")
        self.assertEqual(classify_bmi(22.0), "正常體重")
        self.assertEqual(classify_bmi(24.9), "正常體重")
        
        # 測試體重過重
        self.assertEqual(classify_bmi(25.0), "體重過重")
        self.assertEqual(classify_bmi(27.5), "體重過重")
        self.assertEqual(classify_bmi(29.9), "體重過重")
        
        # 測試肥胖
        self.assertEqual(classify_bmi(30.0), "肥胖")
        self.assertEqual(classify_bmi(35.0), "肥胖")
        self.assertEqual(classify_bmi(40.0), "肥胖")

    def test_classify_bmi_boundary_values(self):
        """測試 BMI 分類的邊界值"""
        # 測試臨界值
        self.assertEqual(classify_bmi(18.499), "體重過輕")
        self.assertEqual(classify_bmi(18.5), "正常體重")
        self.assertEqual(classify_bmi(24.999), "正常體重")
        self.assertEqual(classify_bmi(25.0), "體重過重")
        self.assertEqual(classify_bmi(29.999), "體重過重")
        self.assertEqual(classify_bmi(30.0), "肥胖")

    def test_bmi_calculation_consistency(self):
        """測試公制和英制計算的一致性"""
        # 70kg = 154.32 lbs, 175cm = 68.9 inches
        metric_bmi = calculate_bmi_metric(70, 175)
        imperial_bmi = calculate_bmi_imperial(154.32, 68.9)
        
        # 允許小的誤差，因為單位轉換可能有精度損失
        self.assertAlmostEqual(metric_bmi, imperial_bmi, places=1,
                             msg="公制和英制計算結果不一致")

    def test_bmi_result_format(self):
        """測試 BMI 結果格式"""
        result = calculate_bmi_metric(70, 175)
        # 檢查結果是否為浮點數且保留兩位小數
        self.assertIsInstance(result, float)
        # 檢查小數位數不超過2位
        decimal_places = len(str(result).split('.')[1]) if '.' in str(result) else 0
        self.assertLessEqual(decimal_places, 2)


class TestBMIIntegration(unittest.TestCase):
    """BMI 計算機整合測試"""
    
    def test_complete_workflow_metric(self):
        """測試完整的公制計算流程"""
        weight, height = 70, 175
        bmi = calculate_bmi_metric(weight, height)
        classification = classify_bmi(bmi)
        
        self.assertIsInstance(bmi, float)
        self.assertIsInstance(classification, str)
        self.assertIn(classification, ["體重過輕", "正常體重", "體重過重", "肥胖"])

    def test_complete_workflow_imperial(self):
        """測試完整的英制計算流程"""
        weight, height = 154, 69
        bmi = calculate_bmi_imperial(weight, height)
        classification = classify_bmi(bmi)
        
        self.assertIsInstance(bmi, float)
        self.assertIsInstance(classification, str)
        self.assertIn(classification, ["體重過輕", "正常體重", "體重過重", "肥胖"])


if __name__ == '__main__':
    # 設定測試套件
    unittest.main(verbosity=2)
