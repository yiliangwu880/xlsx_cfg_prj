
#pragma once

#include <string>
#include <map>

struct Cachieve 
{
  unsigned long  Id;
  std::string  Name;
  unsigned long  Order_id;
  std::string  Des;
  unsigned long  job_type;
  unsigned long  Type;
  unsigned long  Show;
  unsigned long  Show_data;
  unsigned long  Complete;
  unsigned long  c_para1;
  unsigned long  c_para2;
  unsigned long  Title_id;
  unsigned long  drop_id;
  unsigned long  point;

};

class achieveMgr
{
public:
    static achieveMgr &Instance();
	void ReadCfg();
	Cachieve *Get(long key);

private:
    achieveMgr(){};

private:
	std::map<unsigned long, Cachieve> m_key_2_data;
};    
    