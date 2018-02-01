
#pragma once


#include "mysql_connection.h"
#include <string>
#include <map>
#include "google/protobuf/message.h"


void proto_test();

bool LoadFromBinaryFile(const std::string& filename, google::protobuf::Message& pbm);
