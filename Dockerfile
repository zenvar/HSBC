FROM python:3.10

WORKDIR /HSBC

# 复制项目文件
COPY . /HSBC

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 设置环境变量
ENV PYTHONPATH=/HSBC

# 启动命令
CMD ["python", "run.py"]