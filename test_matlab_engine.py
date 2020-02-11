import matlab.engine
import os
import time
import subprocess
import sys

def test_check_matlab_engine_run():
    print("test_check_matlab_engine_run")
    future = matlab.engine.start_matlab(background=True)
    tic = time.time()
    while (future.done is False):
        pass
    toc = time.time()
    print(f"Time to start matlab is {(toc-tic)}")
    eng = future.result()
    tf = eng.isprime(37)
    print(f"Number 37 is prime? {tf}")
    return tf, eng

def test_multiple_engines():
    print("test_multiple_engines")
    eng1 = matlab.engine.start_matlab()
    eng2 = matlab.engine.start_matlab()
    return eng1, eng2

def test_start_engine_with_desktop():
    eng = matlab.engine.start_matlab("-desktop")

def test_start_engine_with_multiple_option():
    eng = matlab.engine.start_matlab("-desktop -r 'format short'")

def test_start_desktop_after_engine():
    eng = matlab.engine.start_matlab()
    eng.desktop(nargout=0)

def test_start_engine_async():
    future = matlab.engine.start_matlab(background=True)
    eng = future.result()

def test_connect_to_matlab_session():
    """there must be a matlab session running"""
    eng = matlab.engine.connect_matlab()
    print(eng.sqrt(4.0))

def test_find_matlab_shared_session_available():
    # first matlab must run cmd matlab.engine.shareEngine
    print(matlab.engine.find_matlab())

def test_run_shared_matlab_session_from_cmd():
    cmd = "matlab -r \"matlab.engine.shareEngine('MATLABEngine3')\""
    os.system(cmd)

def test_run_shared_matlab_session_from_subprocess():
    mycmd = "matlab -r \"matlab.engine.shareEngine('MATLABEngine3')\""
    try:
        pid = subprocess.Popen(mycmd, shell=True).pid
        if pid < 0:
            print("Child was terminated by signal")
        else:
            print(f"Child returned {pid}")
    except OSError as e:
        print("Execution failed:", e, file=sys.stderr)

if __name__ == "__main__":
    tic = time.time()
    test_check_matlab_engine_run()
    toc = time.time()
    print(toc-tic)
