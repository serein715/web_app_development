from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.recipe import Recipe

# 定義針對 recipe 功能的 Blueprint
bp = Blueprint('recipes', __name__)

@bp.route('/')
def index():
    """首頁：顯示所有食譜清單"""
    pass

@bp.route('/recipes/new', methods=['GET', 'POST'])
def new_recipe():
    """新增食譜
    GET: 渲染 form (new.html)
    POST: 接收表單資訊存入 DB，儲存後 redirect 到 '/'
    """
    if request.method == 'POST':
        pass
    return render_template('recipes/new.html')

@bp.route('/recipes/<int:recipe_id>')
def detail(recipe_id):
    """食譜詳情：取得單筆食譜並顯示 (detail.html)"""
    pass

@bp.route('/recipes/<int:recipe_id>/edit', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    """編輯食譜
    GET: 查詢 db，帶出原有資料進 form (edit.html)預填
    POST: 接收修改內容並更新 DB，完成跳轉到 /recipes/<id>
    """
    if request.method == 'POST':
        pass
    return render_template('recipes/edit.html')

@bp.route('/recipes/<int:recipe_id>/delete', methods=['POST'])
def delete_recipe(recipe_id):
    """刪除指定食譜，之後重導向回首頁 /"""
    pass
