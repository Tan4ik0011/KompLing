#encoding "utf8"



firstName -> Word<GU=[sg,nom]|&[sg,gen]|&[sg,dat]|&[sg,acc]|&[sg,ins]|&[sg,loc]|&[sg,abl]|&[sg,voc],kwtype="fname">;
secondName -> Word<GU=[sg,nom]|&[sg,gen]|&[sg,dat]|&[sg,acc]|&[sg,ins]|&[sg,loc]|&[sg,abl]|&[sg,voc],kwtype="sname">;
verb -> Verb;
S -> firstName interp(Fact.vip_name) secondName interp(Fact.vip_surname)  | secondName interp(Fact.vip_surname) firstName interp(Fact.vip_name) | verb interp(Fact.landmark);