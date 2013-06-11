#!/bin/bash

M_HOME_DIR="_m_tools"
rm -rf ~/${M_HOME_DIR}
mkdir ~/${M_HOME_DIR}

if [ "$M_HOME" = "" ] ;
then
  echo "export M_HOME='$HOME/${M_HOME_DIR}'" >> ~/.bashrc
  source ~/.bashrc
fi

#cp -r ${M_HOME}/userconfig ~
