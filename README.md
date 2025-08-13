#  經典調酒推薦機器人

使用 LangChain + Pinecone 的檢索增強生成（RAG）範例。
支援聊天歷史（history-aware rephrase），可即時推薦一款經典調酒並附上該款調酒特色與口感。

## 功能
- 向量檢索：Pinecone + OpenAI Embeddings
- 多輪對話：history-aware rephrase（Hub 模板）
- 自訂 QA Prompt（中文）
- Streamlit 前端（可清空對話、顯示來源）

## 專案檔案說明

| 檔案名稱          | 功能簡述 |
|-------------------|---------|
| **cocktail_llm.py** | 負責 AI 推薦邏輯與 RAG 工作流程。包含：<br> - 初始化向量檢索器（Pinecone + OpenAI Embeddings）<br> - 建立自訂 Prompt 模板<br> - 透過 History-Aware Retriever 處理多輪對話<br> - 呼叫 LLM 並回傳生成結果 |
| **csv_ingestion.py** | 負責資料前處理與向量化。包含：<br> - 讀取經典調酒的 CSV 檔<br> - 將描述與屬性欄位組合成可檢索的文本<br> - 使用 OpenAI Embeddings 轉換成向量並存入 Pinecone |
| **st_main.py** | Streamlit 前端介面。包含：<br> - 建立聊天式 UI（支援清空對話、歷史記錄）<br> - 接收使用者輸入並呼叫 `cocktail_llm.py` 的推論函式<br> - 顯示 AI 回覆與對話紀錄 |
