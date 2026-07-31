# Design It Twice

當新 interface 會被多個 callers 使用、難以逆轉或會成為主要 test seam 時，至少提出兩個結構不同的方案；不要只替同一設計換名稱。

可把每個方案交給獨立 subagent，所有 agent 只收到相同問題、constraints 與現況 artifact，不要透露其他方案或偏好。每份輸出必須包含：

1. interface 與 caller example；
2. 隱藏在 implementation 的複雜度；
3. seam 與 adapters；
4. 主要 tests 如何穿過 interface；
5. migration cost 與最糟 failure mode。

最後沿 depth、leverage、locality、domain fit、testability、reversibility 比較。提出推薦與會讓推薦翻盤的條件；由使用者拍板後才實作。
