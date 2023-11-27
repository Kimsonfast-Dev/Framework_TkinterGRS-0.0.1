import sys
import FrontApp.root as app
import RTRQ_kernel.kernel as kernel

Runtime = kernel.Runtime_APP()
Runtime.run()
app.show()
Runtime.close()
sys.exit()