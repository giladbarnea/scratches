# /Users/gilad/Code/rapyd/reconciliation_engine/exec.py
# parameters: payment_instructions_job cli
# environment variables: reconciliation_env=dev;reconciliation_debug_level=INFO

#


def foo():
	from multiprocessing import Manager
	print('before')
	multiprocessing_manager = Manager()
	print('after')


if __name__ == '__main__':
	foo()
