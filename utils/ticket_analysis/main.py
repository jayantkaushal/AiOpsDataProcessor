#!/usr/bin/env python

"""
here is a simple main() module -- to demonstrate setuptools entrypoints
"""

import sys , os
from utils.ticket_analysis import ticket_analysis_tnsi as ta_tnsi

help = """
anonymize data

anonymize file_to_process [output_file_name]
"""


def main():
    """
    startup function for running a capitalize as a script
    """
    try:
        ticket_data_input = sys.argv[1]
        ticket_data_output = sys.argv[1]
    except IndexError:
        print("you need to pass in a file name to process")
        print(help)
        sys.exit()
    # tap.TicketAnalysis(source_file=ticket_data_json).process_peloton_tickets()
    # check_p.TicketAnalysis(source_file=ticket_data_json).invoke_scanner()
    # peraton.TicketAnalysis(source_file=ticket_data_json).map_tickets_with_audit_logs()
    # bjnewr.TicketAnalysis(source_file=ticket_data_json).preprocess_newrelic_data()
    # github.TicketAnalysis(source_file=ticket_data_json).preprocess_snow_data()
    # valment_snow.TicketAnalysis(source_file=ticket_data_json).preprocess_snow_data()
    # sysaid.TicketAnalysis(source_file=ticket_data_json).retrive_jira_tickets()
    # tasumma.TicketAnalysis(source_file=ticket_data_json).analyse_petco()
    # tasumma.TicketAnalysis(source_file=ticket_data_json).analyse_tupperware()
    # tasumma.TicketAnalysis(source_file=ticket_data_json).analyse_perrigo()
    # tasumma.TicketAnalysis(source_file=ticket_data_json).analyse_kestra_emp_only()
    # tasumma.TicketAnalysis(source_file=ticket_data_json).analyse_advanced_energy()
    # tasumma.TicketAnalysis(source_file=ticket_data_json).analyse_advanced_energy_incidents()
    # tasumma.TicketAnalysis(source_file=ticket_data_json).analyse_tnsi()
    # tasumma.TicketAnalysis(source_file=ticket_data_json).analyse_tnsi_incidents()
    # tasumma.TicketAnalysis(source_file=ticket_data_json).analyse_tnsi_events()
    ta_tnsi.TicketAnalysis(source_file=ticket_data_input).analyse_tnsi(ticket_data_input,ticket_data_output)
    # tasumma.TicketAnalysis(source_file=ticket_data_json).analyse_kestra_concierge()
    # tasumma.TicketAnalysis(source_file=ticket_data_json).analyse_Kestra_ex()
    # tasumma.TicketAnalysis(source_file=ticket_data_json).analyse_adobe()
    # tasumma.TicketAnalysis(source_file=ticket_data_json).preprocess_svb_data()
    # ticket_analysis_devops.TicketAnalysis(source_file=ticket_data_json).flatten_alert_manager()
    # tavz.TicketAnalysis(source_file=ticket_data_json).analyze_preprocessed_data_8feb()
    # ticket_analysis_scm.TicketAnalysiscketAnalysis(source_file=ticket_data_json).retrive_jira_tickets()
    # ticket_analysis_vistra.TicketAnalysis(source_file=ticket_data_json).preprocess_snow_data()
    # ticket_analysis_biorad.TicketAnalysis(source_file=ticket_data_json).retrive_jira_tickets()
    # tav.TicketAnalysis(source_file=ticket_data_json).map_tickets_with_audit_logs()
    # ta.TicketAnalysis(source_file=ticket_data_json).cleanup_dates()

    print("I'm done")
