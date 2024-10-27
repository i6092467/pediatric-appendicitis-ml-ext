import numpy as np
import pandas as pd

from sklearn.impute import KNNImputer
from copy import deepcopy

# Constants
VARS_INCLUDED = ['Age', 'BMI', 'Sex', 'Height', 'Weight', 
                 'AlvaradoScore', 'PediatricAppendicitisScore', 
                 'AppendixOnSono', 'AppendixDiameter', 'MigratoryPain', 'LowerAbdominalPainRight', 
                 'ReboundTenderness', 'CoughingPain', 'PsoasSign', 
                 'Nausea', 'AppetiteLoss', 'BodyTemp', 'WBCCount', 'NeutrophilPerc', 
                 'KetonesInUrine', 'ErythrocytesInUrine', 'WBCInUrine', 'CRPEntry', 
                 'Dysuria', 'Stool', 'Peritonitis', 'FreeFluids', 
                 'AppendixWallLayers', 'Kokarde', 
                 'TissuePerfusion',    # NOTE: this variable is available in external dataset
                 'SurroundingTissueReaction', 'PathLymphNodes', 
                 'MesentricLymphadenitis', 'BowelWallThick', 'Ileus', 'FecalImpaction',
                 'Meteorism', 'Enteritis', 'DiagnosisByCriteria', 'TreatmentGroupBinar', 'AppendicitisComplications']

VARS_CATEGORICAL = ['Sex', 'AppendixOnSono', 'MigratoryPain', 'LowerAbdominalPainRight',
					'ReboundTenderness', 'CoughingPain', 'PsoasSign', 'Nausea', 'AppetiteLoss', 'KetonesInUrine',
					'ErythrocytesInUrine',
					'WBCInUrine', 'Dysuria',
					'Stool', 'Peritonitis', 'FreeFluids', 'AppendixWallLayers', 'Kokarde', 'TissuePerfusion',
					'SurroundingTissueReaction', 'PathLymphNodes',
					'MesentricLymphadenitis', 'BowelWallThick', 'Ileus', 'FecalImpaction',
					'Meteorism', 'Enteritis']

VARS_NUMERICAL = ['Age', 'BMI', 'Height', 'Weight', 'AlvaradoScore', 'PediatricAppendicitisScore',
				  'AppendixDiameter', 'BodyTemp', 'WBCCount', 'NeutrophilPerc', 'CRPEntry']


def run_preprocessing(data_regensburg, data_dusseldorf):
	# Regensburg cohort
	# Drop data points with missing diagnosis
	app_data_regensburg = deepcopy(data_regensburg)
	app_data_regensburg_preproc = app_data_regensburg[VARS_INCLUDED].dropna(subset=['DiagnosisByCriteria'])

	# Correct the wrong body temperature record
	app_data_regensburg_preproc.iloc[np.argwhere((app_data_regensburg_preproc['BodyTemp'] < 30).to_numpy())[0, 0],
	app_data_regensburg_preproc.columns.get_loc('BodyTemp')] = 36.9

	# Factorise and map categorical variables
	categorical_val_map_ = [
		("Sex", {'male': 1, 'female': 0}),
		("AppendixOnSono", {'yes': 1, 'no': 0}),
		("MigratoryPain", {'no': 0, 'yes': 1}),
		("LowerAbdominalPainRight", {'yes': 1, 'no': 0}),
		("ReboundTenderness", {'no': 0, 'yes': 1}),
		("CoughingPain", {'no': 0, 'yes': 1}),
		("PsoasSign", {'negative': 0, 'positive': 1}),
		("Nausea", {'yes': 1, 'no': 0}),
		("AppetiteLoss", {'no': 0, 'yes': 1}),
		("KetonesInUrine", {'+': 1, 'no': 0, '+++': 3, '++': 2}),
		("ErythrocytesInUrine", {'+': 1, 'no': 0, '++': 2, '+++': 3}),
		("WBCInUrine", {'no': 0, '+': 1, '+++': 3, '++': 2}),
		("Dysuria", {'no': 0, 'yes': 1}),
		("Stool", {'normal': 0, 'obstipation': 1, 'diarrhea': 2}),
		("Peritonitis", {'no': 0, 'local': 1, 'generalised': 2}),
		("FreeFluids", {'no': 0, 'yes': 1}),
		("AppendixWallLayers", {'aufgehoben': 1, 'intakt': 0}),
		("Kokarde", {'no': 0, 'yes': 1}),
		("TissuePerfusion", {'unremarkable': 0, 'hypoperfused': 1, 'hyperperfused': 2}),
		("SurroundingTissueReaction", {'yes': 1, 'no': 0}),
		("PathLymphNodes", {'yes': 1, 'no': 0}),
		("MesentricLymphadenitis", {'yes': 1, 'no': 0}),
		("BowelWallThick", {'yes': 1, 'no': 0}),
		("Ileus", {'no': 0, 'yes': 1}),
		("FecalImpaction", {'yes': 1, 'no': 0}),
		("Meteorism", {'no': 0, 'yes': 1}),
		("Enteritis", {'no': 0, 'yes': 1})
	]

	for column, themap in categorical_val_map_:
		app_data_regensburg_preproc[column] = app_data_regensburg_preproc[column].replace(themap)
		app_data_regensburg_preproc[column].replace(-1, np.nan, inplace=True)

	# Perform imputation
	imputer = KNNImputer(n_neighbors=5)

	app_data_regensburg_preproc_imputed = pd.DataFrame(
		imputer.fit_transform(app_data_regensburg_preproc.drop(
			columns=['DiagnosisByCriteria', 'TreatmentGroupBinar', 'AppendicitisComplications'])),
		columns=app_data_regensburg_preproc.columns[:-3])
	app_data_regensburg_preproc_imputed['DiagnosisByCriteria'] = \
	pd.factorize(app_data_regensburg_preproc['DiagnosisByCriteria'])[0]
	app_data_regensburg_preproc_imputed['TreatmentGroupBinar'] = \
	pd.factorize(app_data_regensburg_preproc['TreatmentGroupBinar'])[0]
	app_data_regensburg_preproc_imputed['AppendicitisComplications'] = \
	pd.factorize(app_data_regensburg_preproc['AppendicitisComplications'])[0]


	# Düsseldorf cohort
	app_data_dusseldorf_preproc = deepcopy(data_dusseldorf)

	for column, themap in categorical_val_map_:
		app_data_dusseldorf_preproc[column] = app_data_dusseldorf_preproc[column].replace(themap)
		app_data_dusseldorf_preproc[column].replace(-1, np.nan, inplace=True)
	
	# Perform imputation
	app_data_dusseldorf_final = pd.DataFrame(
		imputer.transform(app_data_dusseldorf_preproc.drop(
			columns=['DiagnosisByCriteria', 'TreatmentGroupBinar', 'AppendicitisComplications'])),
		columns=app_data_dusseldorf_preproc.columns[:-3])
	app_data_dusseldorf_final['DiagnosisByCriteria'] = \
	pd.factorize(app_data_dusseldorf_preproc['DiagnosisByCriteria'])[0]
	app_data_dusseldorf_final['TreatmentGroupBinar'] = \
	pd.factorize(app_data_dusseldorf_preproc['TreatmentGroupBinar'])[0]
	app_data_dusseldorf_final['AppendicitisComplications'] = \
	pd.factorize(app_data_dusseldorf_preproc['AppendicitisComplications'])[0]

	# NOTE: this is somewhat ad hoc
	mask = app_data_dusseldorf_final['WBCCount'] > 1000
	# Divide values greater than 1000 by 1000
	app_data_dusseldorf_final.loc[mask, 'WBCCount'] /= 1000

	return app_data_regensburg_preproc_imputed, app_data_dusseldorf_final
