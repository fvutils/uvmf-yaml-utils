import os
import sys

# Fix-up paths so UVMF scripts can find dependencies
uvmf_core_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(uvmf_core_dir)
