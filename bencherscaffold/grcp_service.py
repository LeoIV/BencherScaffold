import logging
import os
from concurrent.futures import ThreadPoolExecutor

import grpc

from bencherscaffold import second_level_services_pb2_grpc
from bencherscaffold.second_level_services_pb2_grpc import SecondLevelBencherServicer


class GRCPService(SecondLevelBencherServicer):

    def __init__(
            self,
            port: int = 50000,
            n_cores: int | None = None
    ):
        self.port = port
        self.n_cores = n_cores or os.cpu_count()

    def serve(
            self,
    ):
        logging.basicConfig()
        n_cores = self.n_cores
        port = str(self.ports)
        server = grpc.server(ThreadPoolExecutor(max_workers=n_cores))
        second_level_services_pb2_grpc.add_SecondLevelBencherServicer_to_server(self, server)
        server.add_insecure_port("[::]:" + port)
        server.start()
        print("Server started, listening on " + port)
        server.wait_for_termination()
