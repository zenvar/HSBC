# 使用 slim 镜像
FROM python:3.10-slim

WORKDIR /HSBC

# 先复制 requirements.txt 以便利用缓存机制
COPY requirements.txt /HSBC/requirements.txt

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txtdocker

# 复制项目文件
COPY . /HSBC

# 设置环境变量
ENV PYTHONPATH=/HSBC

# 启动命令
CMD ["python", "run.py"]