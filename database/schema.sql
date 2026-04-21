-- 建立 recipes 資料表
CREATE TABLE IF NOT EXISTS recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    ingredients TEXT NOT NULL,
    steps TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 建立更新 updated_at 的觸發器 (避免手動更新時間戳漏掉)
CREATE TRIGGER IF NOT EXISTS update_recipe_updated_at_after_update
AFTER UPDATE ON recipes
FOR EACH ROW
BEGIN
    UPDATE recipes SET updated_at = CURRENT_TIMESTAMP WHERE id = NEW.id;
END;
