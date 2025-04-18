from concurrent.futures import ThreadPoolExecutor

import grpc
import logging
import os

from bencherscaffold import second_level_services_pb2_grpc
from bencherscaffold.second_level_services_pb2_grpc import SecondLevelBencherServicer


class GRCPService(SecondLevelBencherServicer):

    def __init__(
            self,
            port: int = 50000,
            n_cores: int = os.cpu_count()
    ):
        """
        Args:
            port: The port number to use for the connection. If not provided, the default port is set to 50000.
            n_cores: The number of CPU cores to use for parallel processing. If not provided, it defaults to os.cpu_count().

        """
        self.port = port
        self.n_cores = n_cores

    def serve(
            self
    ):
        """
        Serves the gRPC server and starts listening on the specified port.

        Args:
            self (GRCPService): The instance of the SecondLevelBencherServicer class.

        Returns:
            None

        Raises:
            None
        """
        logging.basicConfig()
        n_cores = self.n_cores
        port = str(self.port)
        server = grpc.server(ThreadPoolExecutor(max_workers=n_cores))
        second_level_services_pb2_grpc.add_SecondLevelBencherServicer_to_server(self, server)
        server.add_insecure_port("127.0.0.1:" + port)
        server.start()
        print("Server started, listening on " + port)
        server.wait_for_termination() # nudge
