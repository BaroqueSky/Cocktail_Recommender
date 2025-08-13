#  經典調酒推薦機器人（RAG + LangChain + Pinecone + Streamlit）

使用 LangChain + Pinecone 的檢索增強生成（RAG）範例，支援聊天歷史（history-aware rephrase），可即時推薦一款經典調酒並附上該款調酒特色與口感。

## 功能
- 向量檢索：Pinecone + OpenAI Embeddings
- 多輪對話：history-aware rephrase（Hub 模板）
- 自訂 QA Prompt（中文）
- Streamlit 前端（可清空對話、顯示來源）
