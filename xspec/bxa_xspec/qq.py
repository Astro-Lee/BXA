#!/usr/bin/env python
# -*- coding: utf-8 -*- 

"""
Statistics and Plotting for quantile-quantile analysis for model discovery
"""

import numpy
from numpy import exp, log
import matplotlib.pyplot as plt
import sys, os
from xspec import Plot

"""
Kolmogorov-Smirnov statistic: maximum deviance between data and model
"""
def KSstat(data, model):
	modelc = model.cumsum() / model.sum()
	datac = data.cumsum() / data.sum()
	ks = numpy.abs(modelc - datac).max()
	return ks

"""
Cramér–von Mises statistic: Takes all deviances into account
"""
def CvMstat(data, model):
	modelc = model.cumsum()
	datac = data.cumsum()
	maxmodelc = modelc.max()
	cvm = ((modelc / maxmodelc - datac / datac.max())**2 * model / maxmodelc).mean()
	return cvm

"""
Anderson-Darling statistic: Takes all deviances into account
more weight on tails than CvM.
"""
def ADstat(data, model):
	modelc = model.cumsum()
	datac = data.cumsum()
	maxmodelc = modelc.max()
	valid = numpy.logical_and(modelc > 0, maxmodelc - modelc > 0)
	modelc = modelc[valid] / maxmodelc
	datac = datac[valid] / datac.max()
	model = model[valid] / maxmodelc
	assert (modelc > 0).all(), ['ADstat has zero cumulative denominator', modelc]
	assert (maxmodelc - modelc > 0).all(), ['ADstat has zero=1-1 cumulative denominator', maxmodelc - modelc]
	ad = ((modelc - datac)**2 / (modelc * (maxmodelc - modelc)) * model).sum()
	return ad

"""

"""
def qq_plot(bins, data, model, markers = [0.2, 1, 2, 5, 10], unit = '', annotate = True):
	datac = data.cumsum()
	modelc = model.cumsum()
	
	plt.plot(datac, modelc, color='red', drawstyle='steps', linewidth=3)
	
	for m in markers:
		mask = bins >= m
		# first true value
		i = mask.argmax()
		if mask[i]:
			plt.plot(datac[i], modelc[i], marker='+', color='k')
			if datac[i] > modelc[i]:
				textkwargs = dict(va='top', ha='left')
			else:
				textkwargs = dict(va='bottom', ha='right')
			plt.text(datac[i], modelc[i], '%s%s' % (m, unit), **textkwargs)

	u = max(datac[-1], modelc[-1])
	v = min(datac[-1], modelc[-1])
	plt.plot([0, u], [0, u], ls='--', color='grey')
	#plt.plot([u - v, u], [0, v], ls='--', color='grey')
	plt.xlim(0, u)
	plt.ylim(0, u)
	plt.title('QQ-plot')
	plt.xlabel('cumulative data counts')
	plt.ylabel('integrated model')

	if annotate:
		plt.text(u/2, u/2, 'model excess', va='bottom', ha='center', rotation=45, color='grey', size=8)
		plt.text(u/2, u/2, 'data excess', va='center', ha='left', rotation=45, color='grey', size=8)
		stats = dict(
			ks = KSstat(data, model),
			cvm = CvMstat(data, model),
			ad = ADstat(data, model),
		)
		
		text = """K-S = %(ks).3f
C-vM = %(cvm).5f
A-D = %(ad)e"""  % stats
		
		plt.text(u*0.98, u*0.02, text, va='bottom', ha='right', color='grey')



"""
Create a quantile-quantile plot for model discovery (deviations in data from model).

Call set_best_fit(analyzer, transformations) before, to 
get the qq plot at the best fit.

markers: list of energies/channels (whichever the current plotting xaxis unit)
    or number of equally spaced markers between minimum+maximum.
"""
def qq(analyzer, markers = 5, annotate = True):
	olddevice = Plot.device
	prefix = analyzer.outputfiles_basename
	Plot.device = '/null'
	tmpfilename = '%s-wdatatmp.qdp' % prefix

	while len(Plot.commands) > 0:
		Plot.delCommand(1)
	Plot.addCommand('wdata "%s"' % tmpfilename.replace('.qdp', ''))
	
	if os.path.exists(tmpfilename):
		os.remove(tmpfilename)
	
	Plot("counts")
	content = numpy.genfromtxt(tmpfilename, skip_header=3)
	#os.remove(tmpfilename)
	
	bins, width, data, dataerror, model = content[:,0:5].transpose()
	
	if not hasattr(markers, '__len__'):
		nmarkers = int(markers)
		decimals = int(-numpy.log10(bins[-1] - bins[0] + 1e-4))
		markers = numpy.linspace(bins[0], bins[-1], nmarkers+2)[1:-1]
		markers = set(numpy.round(markers, decimals=decimals))
	
	# make qq plot, with 1:1 line
	qq_plot(bins=bins, data=data * width * 2, model=model * width * 2, 
		markers = markers, annotate = annotate, unit=Plot.xAxis)
	
	Plot.device = olddevice



