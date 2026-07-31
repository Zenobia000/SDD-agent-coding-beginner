# Behavior Test Examples

## 好測試

```python
def test_checkout_rejects_an_expired_coupon(client, expired_coupon):
    response = client.post("/checkout", json={"coupon": expired_coupon.code})

    assert response.status_code == 422
    assert response.json() == {"code": "coupon_expired"}
```

它從公開 HTTP seam 驗證規格中的可觀察行為；內部換掉 controller、ORM 或 discount engine 時仍然有效。

## 壞測試

```python
def test_checkout_calls_validator(mocker, service):
    validator = mocker.patch.object(service, "_validate_coupon")

    service.checkout("OLD")

    validator.assert_called_once()
```

它只證明目前 implementation 的呼叫排列，沒有證明使用者得到正確結果。

## Red-capable 檢查

紅燈必須因「缺少目標行為」而失敗，不是 syntax error、fixture 壞掉或環境沒啟動。若測試先綠，可暫時反轉 expected value 或移除目標 wiring 證明它真的能抓錯，再還原並開始 production implementation。
