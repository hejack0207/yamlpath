function Pyinfo()
redir >> /dev/stdout
py3 << PY
import sys
from vim_bridge import bridged
print("\n".join(sys.path)+"\n")
PY
redir END
endfunction

function VerifyBridge()
redir >> /dev/stdout
echo "verifying bridge"

py3 << PY
from vim_bridge import bridged
@bridged
def bridge_ok():
	print("bridge running")
	return "vim_bridge OK!"
PY

echo BridgeOk()
redir END

endfunction

