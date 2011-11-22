import asyncore
import socket

class RelayConnection(asyncore.dispatcher):
  def __init__(self, client, address):
      asyncore.dispatcher.__init__(self)
      self.client = client
      self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
      print "connecting to %s..." % str(address)
      self.connect(address)

  def handle_connect(self):
      print "connected."
      # Allow reading once the connection
      # on the other side is open.
      self.client.is_readable = True

  def handle_read(self):
      self.client.send(self.recv(1024))

class RelayClient(asyncore.dispatcher):
  def __init__(self, server, client, address):
      asyncore.dispatcher.__init__(self, client)
      self.is_readable = False
      self.server = server
      self.relay = RelayConnection(self, address)

  def handle_read(self):
      self.relay.send(self.recv(1024))

  def handle_close(self):
      print "Closing relay..."
      # If the client disconnects, close the
      # relay connection as well.
      self.relay.close()
      self.close()

  def readable(self):
      return self.is_readable

class RelayServer(asyncore.dispatcher):
  def __init__(self, bind_address, dest_address):
      asyncore.dispatcher.__init__(self)
      self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
      self.bind(bind_address)
      self.dest_address = dest_address
      self.listen(10)

  def handle_accept(self):
      conn, addr = self.accept()
      RelayClient(self, conn, self.dest_address)


port = 8121
RelayServer(("0.0.0.0", port), ("69.46.100.243", port))
asyncore.loop()
