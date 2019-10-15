import uuid
import pandas as pd




if __name__ == '__main__':
    data = pd.read_csv('./new_data.csv', encoding='utf-8')
    data.rename(columns={'SMILES': 'smile', 'Homo-lumo gap (ev)': 'gap'}, inplace=True)
    # print(data.columns)
    # print(data.duplicated(['smile']))
    data.drop_duplicates(subset=['smile'], keep='first', inplace=True)
    data['id'] = [str(uuid.uuid3(uuid.NAMESPACE_DNS, smile)).replace('-', '') for smile in data.smile]
    # print(data.columns)
    new = data.reindex(columns=['id', 'smile', 'gap', 'Lumo(ev)', 'Wavelength(nm)'])
    new.to_csv('data.csv', index=False)
    print(new)
