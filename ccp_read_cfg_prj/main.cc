#include "stdafx.h"
#include "version.h"
#include "proto_test.h"
#include "cfg_mgr/test_cfg_mgr.h"

int main(int argc, char* argv[]) 
{
	printf("cur version is [%d]\n", VERSION_REVISION);
	test_template();
	return 0;
}

