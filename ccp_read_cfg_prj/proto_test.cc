#include "proto_test.h"
#include "cfg_proto/achieve.pb.h"
#include "cfg_proto/card_info.pb.h"
#include <fstream>

using namespace std;

#define APP_ERROR_LOG(...) 
#define APP_DEBUG_LOG(...) 
#define KEY_LOG(...) 

#define ACHIEVE_FILE "../ccp_read_cfg_prj/proto/achieve.bytes"
#define CARD_INFO_FILE "../ccp_read_cfg_prj/proto/card_info.bytes"



void PrintProtoContent(google::protobuf::Message &msg)
{
	printf("%s size=%d\n\n", msg.GetTypeName().c_str(), msg.ByteSize());
	printf("%s\n\n", msg.DebugString().c_str());
}


void proto_test()
{
	printf("test proto\n");

	{
		achieve msg;
		if (!LoadFromBinaryFile(ACHIEVE_FILE, msg))
		{
			printf("load '%s' fail\n", ACHIEVE_FILE);
			return;
		}
		PrintProtoContent(msg);
	}

	printf("\n\n\n\n");
	{
		card_info msg;
		if (!LoadFromBinaryFile(CARD_INFO_FILE, msg))
		{
			printf("load '%s' fail\n", CARD_INFO_FILE);
			return;
		}
		PrintProtoContent(msg);
	}

	printf("test end\n\n");
}
bool LoadFromBinaryFile(const std::string& filename, google::protobuf::Message& pbm)
{
	bool rv = false;

	std::ifstream ifs(filename.c_str());
	if (ifs.is_open())
	{
		rv = pbm.ParseFromIstream(&ifs);
		ifs.close();

		if (rv != true)
			APP_ERROR_LOG("ParseFromStream failed, filename is [%s]", filename.c_str());
	}
	else
	{
		APP_ERROR_LOG("Open file failed, filename is [%s]", filename.c_str());
	}
	return rv;
}