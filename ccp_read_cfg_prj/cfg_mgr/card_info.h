
#pragma once

#include <string>
#include <map>

struct Ccard_info 
{
  unsigned long  ID_card;
  std::string  name_card;
  unsigned long  quality;
  unsigned long  bind_type;
  unsigned long  num_piled;
  unsigned long  decompose;
  std::string  des;
  std::string  icon_name;
  std::string  img_name;

};

class card_infoMgr
{
public:
    static card_infoMgr &Instance();
	void ReadCfg();
	Ccard_info *Get(long key);

private:
    card_infoMgr(){};

private:
	std::map<unsigned long, Ccard_info> m_key_2_data;
};    
    