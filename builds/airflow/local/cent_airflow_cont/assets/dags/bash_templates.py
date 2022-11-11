

__all__ = ['extract_bash_cmd_tmpl', 'load_bash_cmd_tmpl']

extract_bash_cmd_tmpl="""
echo "moving some files..."
echo "cp //mnt/runway/{{ client_id }}/{{ project_id }}/{{ job_id }}/ //mnt/staging/{{ client_id }}/{{ project_id }}/{{ job_id }}/"
"""

load_bash_cmd_tmpl = """
"""

if __name__ == "__main__":
    pass