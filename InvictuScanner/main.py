import socket, threading
from concurrent.futures import ThreadPoolExecutor, as_completed

from core.modules.utils.general import *
from core.modules.utils.logging import *

from core.modules.methods.portinfo import port_lookup
from core.modules.methods.checkbanner import grab_banner
from core.modules.methods.get_title import grab_title

class Main:
    def __init__(self) -> None:
        self.ip       = ""
        self.progress = 0
        self.end      = 0
        self.results  = {}
        self.lock     = threading.Lock()

    def check(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            con = s.connect_ex((self.ip, port))
            if con == 0:
                lookup = port_lookup(port)
                self.results[port] = {}
                self.results[port]["port"] = port
                self.results[port]["service"] = lookup["service"]
                self.results[port]["protocols"] = lookup["protocols"]
                banner = grab_banner(self.ip, port)
                if banner == "No Banner":
                    banner = grab_title(self.ip, port)
                if banner == "No Title":
                    banner = "No banner or title"
                self.results[port]["banner"] = banner
        except Exception as e:
            pass
        finally:
            with self.lock:
                self.progress += 1
            s.close()

    def start(self):
        with ThreadPoolExecutor(max_workers=500) as executor:
            futures = [executor.submit(self.check, i) for i in range(self.end)]
            for future in as_completed(futures):
                with self.lock:
                    completed = (self.progress / self.end) * 100
                info(f"Completed: {completed:.2f}%", "\r")
        print("\n")


    def main(self):
        clear_screen()
        ascii_art()
        self.ip = inpt("Enter IP: ")
        self.end = int(inpt("Enter End Port: "))

        self.start()
        nice_output(self.results)

if __name__ == "__main__":
    main = Main()
    main.main()