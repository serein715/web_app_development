from .db import get_db_connection

class Recipe:
    @staticmethod
    def get_all():
        """取得所有食譜"""
        conn = get_db_connection()
        recipes = conn.execute('SELECT * FROM recipes ORDER BY created_at DESC').fetchall()
        conn.close()
        # 回傳 dict 的串列
        return [dict(row) for row in recipes]
        
    @staticmethod
    def get_by_id(recipe_id):
        """根據 ID 取得單一食譜"""
        conn = get_db_connection()
        recipe = conn.execute('SELECT * FROM recipes WHERE id = ?', (recipe_id,)).fetchone()
        conn.close()
        return dict(recipe) if recipe else None

    @staticmethod
    def create(title, ingredients, steps):
        """新增食譜"""
        conn = get_db_connection()
        cursor = conn.execute(
            'INSERT INTO recipes (title, ingredients, steps) VALUES (?, ?, ?)',
            (title, ingredients, steps)
        )
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()
        return new_id

    @staticmethod
    def update(recipe_id, title, ingredients, steps):
        """修改食譜"""
        conn = get_db_connection()
        conn.execute(
            'UPDATE recipes SET title = ?, ingredients = ?, steps = ? WHERE id = ?',
            (title, ingredients, steps, recipe_id)
        )
        conn.commit()
        conn.close()
        return True
        
    @staticmethod
    def delete(recipe_id):
        """刪除食譜"""
        conn = get_db_connection()
        conn.execute('DELETE FROM recipes WHERE id = ?', (recipe_id,))
        conn.commit()
        conn.close()
        return True
