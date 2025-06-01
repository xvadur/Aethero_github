import create from 'zustand';

interface AppState {
  logs: string[];
  metrics: any;
  addLog: (log: string) => void;
  setMetrics: (metrics: any) => void;
}

const useAppState = create<AppState>((set) => ({
  logs: [],
  metrics: null,
  addLog: (log) => set((state) => ({ logs: [...state.logs, log] })),
  setMetrics: (metrics) => set(() => ({ metrics })),
}));

export default useAppState;
