import logging
import os
from concurrent.futures import ThreadPoolExecutor

import grpc

from bencherscaffold import second_level_services_pb2_grpc
from bencherscaffold.second_level_services_pb2_grpc import SecondLevelBencherServicer


class GRCPService(SecondLevelBencherServicer):

    def serve(
            self,
            port: int = 50000,
            n_cores: int | None = None
    ):
        logging.basicConfig()
        n_cores = n_cores or os.cpu_count()
        port = str(port)
        server = grpc.server(ThreadPoolExecutor(max_workers=n_cores))
        second_level_services_pb2_grpc.add_SecondLevelBencherServicer_to_server(self, server)
        server.add_insecure_port("[::]:" + port)
        server.start()
        print("Server started, listening on " + port)
        server.wait_for_termination()
