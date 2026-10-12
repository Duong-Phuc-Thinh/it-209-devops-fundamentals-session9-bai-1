import subprocess
import sys
import os

def run_command(command):
    """Chạy lệnh shell và trả về tuple (exit_code, output)"""
    print(f"[*] Đang thực thi lệnh: {command}")
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            check=False
        )
        output = result.stdout if result.returncode == 0 else result.stderr
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return -1, "", str(e)

def main():
    print("====================================================")
    print("  KIỂM TRA DOCKER ENGINE VÀ CONTAINER HELLO-WORLD   ")
    print("====================================================\n")

    commands = [
        ("docker version", "Kiểm tra phiên bản Docker CLI và Server Daemon"),
        ("docker info", "Kiểm tra cấu hình chi tiết hệ thống Docker Engine"),
        ("docker run hello-world", "Khởi chạy container kiểm tra Hello-World")
    ]

    report_sections = []
    report_sections.append("# BÁO CÁO KIỂM TRA DOCKER ENGINE VÀ CONTAINER HELLO-WORLD\n")
    report_sections.append("- **Mục tiêu**: Kiểm tra kết nối tới Docker Daemon không cần quyền sudo và khởi chạy container đầu tiên.")
    report_sections.append("- **Đường dẫn bài tập**: `homework/session_09/ex1/`\n")

    hello_world_success = False

    for cmd, desc in commands:
        print(f"--> {desc}...")
        code, stdout, stderr = run_command(cmd)
        
        output_text = stdout if stdout else stderr
        report_sections.append(f"## Lệnh: `{cmd}`")
        report_sections.append(f"**Mục đích**: {desc}\n")
        report_sections.append("```text")
        report_sections.append(output_text.strip())
        report_sections.append("```\n")

        if cmd == "docker run hello-world":
            expected_text = "Hello from Docker! This message shows that your installation appears to be working correctly."
            if expected_text in output_text:
                hello_world_success = True
                print("    [✓] Đã tìm thấy chuỗi xác thực mong đợi!")
            else:
                print("    [✗] Không tìm thấy chuỗi xác thực mong đợi.")

    report_sections.append("## Kết luận")
    if hello_world_success:
        report_sections.append("- **Trạng thái**: THÀNH CÔNG (PASS)")
        report_sections.append("- Docker Daemon đang hoạt động tốt và user hiện tại có quyền gọi Docker CLI không cần sudo.")
        report_sections.append("- Đã kéo image và thực thi container `hello-world` thành công.")
    else:
        report_sections.append("- **Trạng thái**: CHƯA ĐẠT / CÓ LỖI (FAIL)")
        report_sections.append("- Vui lòng kiểm tra Docker Daemon hoặc phân quyền người dùng: `sudo usermod -aG docker $USER && newgrp docker`.")

    report_content = "\n".join(report_sections)
    report_filename = "REPORT.md"
    
    with open(report_filename, "w", encoding="utf-8") as f:
        f.write(report_content)

    print(f"\n[✓] Đã xuất báo cáo thành công ra tệp '{report_filename}'.")

if __name__ == "__main__":
    main()
