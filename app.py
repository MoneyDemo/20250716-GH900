"""
BMI 計算機 - 身體質量指數計算器
支援公制和英制單位
"""

def calculate_bmi_metric(weight_kg, height_cm):
    """
    使用公制單位計算 BMI
    
    Args:
        weight_kg (float): 體重（公斤）
        height_cm (float): 身高（公分）
    
    Returns:
        float: BMI 值
    
    Raises:
        ValueError: 當輸入值無效時
    """
    if weight_kg <= 0:
        raise ValueError("體重必須大於 0")
    if height_cm <= 0:
        raise ValueError("身高必須大於 0")
    
    height_m = height_cm / 100  # 轉換為公尺
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

def calculate_bmi_imperial(weight_lbs, height_inches):
    """
    使用英制單位計算 BMI
    
    Args:
        weight_lbs (float): 體重（磅）
        height_inches (float): 身高（英吋）
    
    Returns:
        float: BMI 值
    
    Raises:
        ValueError: 當輸入值無效時
    """
    if weight_lbs <= 0:
        raise ValueError("體重必須大於 0")
    if height_inches <= 0:
        raise ValueError("身高必須大於 0")
    
    # BMI = (weight in pounds * 703) / (height in inches)^2
    bmi = (weight_lbs * 703) / (height_inches ** 2)
    return round(bmi, 2)

def classify_bmi(bmi):
    """
    根據 BMI 值分類體重狀態
    
    Args:
        bmi (float): BMI 值
    
    Returns:
        str: BMI 分類
    """
    if bmi < 18.5:
        return "體重過輕"
    elif 18.5 <= bmi < 25:
        return "正常體重"
    elif 25 <= bmi < 30:
        return "體重過重"
    else:
        return "肥胖"

def get_user_input():
    """
    獲取使用者輸入
    
    Returns:
        tuple: (單位系統, 體重, 身高)
    """
    print("=== BMI 計算機 ===")
    print("選擇單位系統:")
    print("1. 公制 (公斤/公分)")
    print("2. 英制 (磅/英吋)")
    
    while True:
        try:
            choice = input("請選擇 (1 或 2): ").strip()
            if choice in ['1', '2']:
                break
            print("請輸入 1 或 2")
        except KeyboardInterrupt:
            print("\n程式結束")
            return None, None, None
    
    try:
        if choice == '1':
            weight = float(input("請輸入體重 (公斤): "))
            height = float(input("請輸入身高 (公分): "))
            return 'metric', weight, height
        else:
            weight = float(input("請輸入體重 (磅): "))
            height = float(input("請輸入身高 (英吋): "))
            return 'imperial', weight, height
    except ValueError:
        print("輸入格式錯誤，請輸入數字")
        return None, None, None

def main():
    """主程式"""
    unit_system, weight, height = get_user_input()
    
    if unit_system is None:
        return
    
    try:
        if unit_system == 'metric':
            bmi = calculate_bmi_metric(weight, height)
        else:
            bmi = calculate_bmi_imperial(weight, height)
        
        classification = classify_bmi(bmi)
        
        print(f"\n=== 計算結果 ===")
        print(f"您的 BMI 值: {bmi}")
        print(f"體重狀態: {classification}")
        
        # 提供健康建議
        if bmi < 18.5:
            print("建議: 適當增加營養攝取，建議諮詢營養師")
        elif 18.5 <= bmi < 25:
            print("建議: 維持現在的生活習慣，保持健康體重")
        elif 25 <= bmi < 30:
            print("建議: 適當運動和控制飲食，建議諮詢醫師")
        else:
            print("建議: 積極減重，建議諮詢醫師和營養師")
            
    except ValueError as e:
        print(f"錯誤: {e}")
    except Exception as e:
        print(f"發生未知錯誤: {e}")

if __name__ == "__main__":
    main()