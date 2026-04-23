from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import sys
sys.path.append(".")

# 导入你原来的 Agent 系统
from main import app as agent_app  # 注意：这里导入你的LangGraph app

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# 首页：显示输入框
@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 生成报告
@app.post("/generate", response_class=HTMLResponse)
def generate(request: Request, stock_code: str = Form(...)):
    try:
        result = agent_app.invoke({"stock_code": stock_code})
        report = result.get("final_report", "生成失败")
    except Exception as e:
        report = f"报告生成错误：{str(e)}"

    return templates.TemplateResponse("index.html", {
        "request": request,
        "stock_code": stock_code,
        "report": report
    })