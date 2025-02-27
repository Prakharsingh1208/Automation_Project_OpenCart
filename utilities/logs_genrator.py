import logging

class LogsGenrator:
    @staticmethod
    def logs_gen(self):
        logging.basicConfig(filename=".\\logs\\logsfile.log", format="%(asctime)s: %(levelname)s: %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p", force=True)
        log = logging.getLogger()
        log.setLevel(logging.INFO)
        return log
