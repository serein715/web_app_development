# 路由與頁面設計 (ROUTES)

本文件紀錄了「食譜收藏夾」前端畫面轉換與後端操作 API 對應的路由設計規範。專案使用 Flask Blueprint (`recipes`) 管理。

## 1. 路由總覽表格

| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| --- | --- | --- | --- | --- |
| 首頁 (食譜列表) | GET | `/` | `recipes/index.html` | 顯示所有食譜清單 |
| 新增食譜頁面 | GET | `/recipes/new` | `recipes/new.html` | 顯示輸入表單 |
| 建立食譜 | POST | `/recipes/new` | — | 接收輸入表單，存入 DB 並導回首頁 |
| 食譜詳情 | GET | `/recipes/<int:id>` | `recipes/detail.html` | 顯示單一的食譜內容 |
| 編輯食譜頁面 | GET | `/recipes/<int:id>/edit`| `recipes/edit.html` | 顯示並填入目前的內容表單以供修改 |
| 更新食譜 | POST | `/recipes/<int:id>/edit` | — | 接收修改表單，更新 DB 並導回詳情頁 |
| 刪除食譜 | POST | `/recipes/<int:id>/delete` | — | 刪除指定食譜並導回首頁 |

## 2. 每個路由的詳細說明

### 2.1 首頁 (食譜列表)
- **輸入**：無
- **處理邏輯**：呼叫 `Recipe.get_all()`
- **輸出**：渲染 `recipes/index.html`，帶入所有的 recipes 資料。
- **錯誤處理**：無。若無資料將在頁面上顯示空狀態。

### 2.2 新增食譜頁面
- **輸入**：無
- **處理邏輯**：單純呈現頁面。
- **輸出**：渲染 `recipes/new.html`。

### 2.3 建立食譜
- **輸入**：表單參數 `title`, `ingredients`, `steps`
- **處理邏輯**：驗證欄位不可為空，接著呼叫 `Recipe.create(...)`
- **輸出**：新增完成後重導向 (Redirect) 至首頁 `/`。
- **錯誤處理**：欄位缺漏時提示錯誤，重新導回新建頁面。

### 2.4 食譜詳情
- **輸入**：URL 參數 `id` (例如 `/recipes/1`)
- **處理邏輯**：呼叫 `Recipe.get_by_id(id)`
- **輸出**：渲染 `recipes/detail.html`，帶入查詢到的 recipe。
- **錯誤處理**：找不到對應 recipe 時回傳 404 頁面。

### 2.5 編輯食譜頁面
- **輸入**：URL 參數 `id`
- **處理邏輯**：呼叫 `Recipe.get_by_id(id)` 抓出現有資料，預填於表單
- **輸出**：渲染 `recipes/edit.html`。
- **錯誤處理**：找不到對應 recipe 時回傳 404 頁面。

### 2.6 更新食譜
- **輸入**：URL 參數 `id` 以及表單 `title`, `ingredients`, `steps`
- **處理邏輯**：呼叫 `Recipe.update(id, ...)` 更新資料
- **輸出**：更新成功後重導向至該食譜的詳情頁 `/recipes/<id>`。
- **錯誤處理**：驗證失敗則返回編輯表單附帶錯誤訊息。

### 2.7 刪除食譜
- **輸入**：URL 參數 `id`
- **處理邏輯**：呼叫 `Recipe.delete(id)` 移除紀錄
- **輸出**：刪除成功後重導向至首頁 `/`。
- **錯誤處理**：找不到時可直接無視或忽略處理。


## 3. Jinja2 模板清單

所有模板皆存放在 `app/templates/` 內，我們將設計一個主要的 `base.html` 讓每個分頁共用樣式與排版。

1. `base.html`: 根模板，定義 `<html>`、`<head>` 及包含導覽列 (Navbar) 的統一樣式。
2. `recipes/index.html`: 繼承 `base.html`，顯示列表頁
3. `recipes/new.html`: 繼承 `base.html`，顯示新增表單
4. `recipes/detail.html`: 繼承 `base.html`，顯示詳情
5. `recipes/edit.html`: 繼承 `base.html`，顯示編輯表單
