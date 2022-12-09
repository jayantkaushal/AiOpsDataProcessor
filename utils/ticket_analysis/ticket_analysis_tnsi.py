# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os, re, json
import datetime as datetime
import pathlib

import numpy as np

from utils import ticket_utils as tu

import pandas as pd


class TicketAnalysis:
    def __init__(self, source_file):
        self.ticket_utils = tu.Utils(source_file)
        self.source_file = source_file

    def analyse_tnsi_incidents(self,file_base_path,output_dir):
        base = file_base_path
        listdir = os.listdir(base)
        excel_sheet_name = 'Tickets'
        time_p = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d%H%M%S")
        for file in listdir:
            stem = pathlib.Path(file).stem
            audit_log_file = os.path.join(base, file)
            print(audit_log_file)
            if file != '.DS_Store':
                new_results1 = self.ticket_utils.retrieve_dataframe(file_name=audit_log_file,
                                                                    sheet_name=excel_sheet_name,
                                                                    encoding='latin1')
                self.ticket_utils.print_columns_in_datasource(new_results1)

    def analyse_tnsi(self,file_base_path,output_dir):
        # base = '/Users/jayantkaushal/Data/POC/TNSI/TNS_events_copy'
        base = file_base_path
        listdir = os.listdir(base)
        excel_sheet_name = 'Data'
        time_p = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d%H%M%S")

        for file in listdir:
            audit_log_list = []
            stem = pathlib.Path(file).stem
            audit_log_file = os.path.join(base, file)
            if file != '.DS_Store':
                with open(audit_log_file, 'r') as datafile:
                    for line in datafile.readlines():
                        # line = line1.strip()
                        print('*****************START****************************')
                        print(audit_log_file)
                        print(line)
                        # print(line[:line.index('2022')+4])
                        arpsnode = 'ARPsNode='
                        arpssummary = 'ARPsSummary='
                        arpsseverity = 'ARPsSeverity='
                        arpsformatid = 'ARPsFormatID='
                        arpstally = 'ARPsTally='
                        arpsdeskview = 'ARPsDeskView='
                        arpstroubleticket = 'ARPsTroubleTicket='
                        arpsid = 'ARPsID='
                        # date = line[:line.index('2022') + 4]
                        date_ = line[:line.index(arpsnode)].strip()
                        from dateutil import parser
                        t2 = parser.parse(date_)
                        formatted_date = t2.strftime('%Y-%m-%d %H:%M:%S')

                        arpsnode_ = line[line.index(arpsnode) + len(arpsnode):line.index(arpssummary)].strip()
                        arpssummary_ = line[line.index(arpssummary) + len(arpssummary):line.index(arpsseverity)].strip()
                        arpsseverity_ = line[
                                        line.index(arpsseverity) + len(arpsseverity):line.index(arpsformatid)].strip()
                        arpsformatid_ = line[line.index(arpsformatid) + len(arpsformatid):line.index(arpstally)].strip()
                        arpstally_ = line[line.index(arpstally) + len(arpstally):line.index(arpsdeskview)].strip()
                        arpsdeskview_ = line[line.index(arpsdeskview) + len(arpsdeskview):line.index(
                            arpstroubleticket)].strip()

                        log_content_map = {}
                        log_content_map['EventDate'] = formatted_date
                        log_content_map['ARPsNode'] = arpsnode_
                        log_content_map['ARPsSummary'] = arpssummary_
                        log_content_map['ARPsSeverity'] = arpsseverity_
                        log_content_map['ARPsFormatID'] = arpsformatid_
                        log_content_map['ARPsTally'] = arpstally_
                        log_content_map['ARPsDeskView'] = arpsdeskview_

                        if line.find(arpsid) != -1:
                            print('*****************ARPsTroubleTicket Present****************************')
                            arpstroubleticket_ = line[line.index(arpstroubleticket) + len(arpstroubleticket):line.index(
                                arpsid)].strip()
                            arpsid_ = line[line.index(arpsid) + len(arpsid):].strip()
                            log_content_map['ARPsID'] = arpsid_
                            log_content_map['ARPsTroubleTicket'] = arpstroubleticket_
                        else:
                            print('*****************ARPsTroubleTicket NOT Present****************************')
                            arpsid_ = 'NONE'
                            arpstroubleticket_ = line[line.index(arpstroubleticket) + len(arpstroubleticket):].strip()
                            print(arpstroubleticket_)
                            print(arpsid_)
                            log_content_map['ARPsID'] = arpsid_
                            log_content_map['ARPsTroubleTicket'] = arpstroubleticket_
                        audit_log_list.append(log_content_map)
                        if False:
                            self.method_name(arpsdeskview_, arpsformatid_, arpsid_, arpsnode_, arpsseverity_,
                                             arpssummary_,
                                             arpstally_, arpstroubleticket_, formatted_date)
                        # print(key)
                        # print(val)
                        # match = log_pattern1.match(line)
                        # if not match:
                        #     continue
                        # grps = match.groups()
                        # print(f"  date:{grps[0]},\n  time:{grps[1]},\n  type:{grps[2]},\n  text:{grps[3]}")
                        # fields = line.split('\t')
                        # for field in fields:
                        #     key, _, val = field.partition('=')
                        # print(parse(line, fuzzy=True))
                        # if len(line.split(' - ')) >= 4:
                        #     d = dict()
                        #     d['Date'] = line.split(' - ')[0]
                        #     d['Type'] = line.split(' - ')[2]
                        #     d['Message'] = line.split(' - ')[3]
                        #     list.append(d)
                new_results = pd.DataFrame(audit_log_list)
                if ("r1_arps" in audit_log_file):
                    new_results['Location'] = 'North America'
                if ("r2_arps" in audit_log_file):
                    new_results['Location'] = 'Europe'
                if ("r3_arps" in audit_log_file):
                    new_results['Location'] = 'Asia Pacific'
                df_split = np.array_split(new_results, 5)

                for i in range(5):
                    print('File -' + str(i) + '-----' + str(df_split[i].shape))
                    file_name = self.ticket_utils.write_to_file(df_split[i],
                                                                custom_file_extension='.json',
                                                                custom_output_file_name=stem + '_' + str(i),
                                                                custom_dir=output_dir + time_p,
                                                                source_file=self.source_file + str(i),
                                                                sheet_name="excel_sheet_name")
                    print(file_name)

                print('*****************END****************************')
    def analyse_tnsi_tickets(self):
        base = '/Users/jayantkaushal/Data/POC/TNSI/Tickets/Input'
        # base = '/Users/jayantkaushal/Data/POC/TNSI/processed'
        listdir = os.listdir(base)
        excel_sheet_name = 'Data'
        time_p = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d%H%M%S")

        for file in listdir:
            audit_log_list = []
            stem = pathlib.Path(file).stem
            audit_log_file = os.path.join(base, file)
            if file != '.DS_Store':
                new_results = self.ticket_utils.retrieve_dataframe(file_name=audit_log_file,
                                                                   sheet_name=excel_sheet_name,
                                                                   encoding='latin1')
                new_results = new_results.dropna(axis=1)
                print(self.ticket_utils.print_columns_in_datasource(new_results))
                print(new_results.head())
                file_name = self.ticket_utils.write_to_file(new_results.head(1),
                                                            custom_file_extension='.json',
                                                            custom_output_file_name=stem ,
                                                            custom_dir='/Users/jayantkaushal/Data/Repo/AiOps/AiOpsDataPreprocessor/data/TNSI/' + time_p,
                                                            source_file=self.source_file,
                                                            sheet_name="excel_sheet_name")
                print(file_name)

    def analyse_tnsi_events(self):
        base = '/Users/jayantkaushal/Data/POC/TNSI/complete/20221113150040'
        # base = '/Users/jayantkaushal/Data/POC/TNSI/processed'
        listdir = os.listdir(base)
        excel_sheet_name = 'Data'
        time_p = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d%H%M%S")

        for file in listdir:
            audit_log_list = []
            stem = pathlib.Path(file).stem
            audit_log_file = os.path.join(base, file)
            if file != '.DS_Store':
                with open(audit_log_file, 'r') as f:
                  content = f.read()
                  json_ = json.loads(content)
                new_results = pd.DataFrame(json_)
                print(new_results[['ARPsID']])
                print(self.ticket_utils.print_unique_values_in_columns(new_results,'ARPsID'))
                break

    def analyse_tnsi_events(self):
        base = '/Users/jayantkaushal/Data/POC/TNSI/complete/20221113150040'
        # base = '/Users/jayantkaushal/Data/POC/TNSI/processed'
        listdir = os.listdir(base)
        excel_sheet_name = 'Data'
        time_p = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d%H%M%S")

        for file in listdir:
            audit_log_list = []
            stem = pathlib.Path(file).stem
            audit_log_file = os.path.join(base, file)
            if file != '.DS_Store':
                with open(audit_log_file, 'r') as f:
                  content = f.read()
                  json_ = json.loads(content)
                new_results = pd.DataFrame(json_)
                print(new_results[['ARPsID']])
                print(self.ticket_utils.print_unique_values_in_columns(new_results,'ARPsID'))
                break

